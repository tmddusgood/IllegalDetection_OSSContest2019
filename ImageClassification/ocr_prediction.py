import cv2
import numpy as np
import math
import os
import tensorflow as tf
import pytesseract


class Assistant:
    def __init__(self):
        self.MODEL_PATH = 'ImageClassification/output_graph.pb'
        self.LABELS_PATH = 'ImageClassification/output_labels.txt'
        self.ASPECT_RATIO_THRESHOLD = 5.0
        self.SOLIDITY_THRESHOLD = 0.4
        self.EXTENT_MIN_THRESHOLD = 0.23
        self.EXTENT_MAX_THRESHOLD = 0.90
        self.COMPACTNESS_MIN_THRESHOLD = 3e-3
        self.COMPACTNESS_MAX_THRESHOLD = 1e-1

    def COMPACTNESS(self, region, perimeter):
        """
        Calculate compactness of region
        COMPACTNESS=area/perimeter*perimeter
        """
        area = len(list(region))  # area= number of pixels in region
        if 0 == perimeter:  # division by zero
            return -1
        compacteness = (1.0 * area) / (perimeter * perimeter)
        return compacteness

    def PERIMETER(self, img, region):
        """
        Calculate perimeter of region
        PERIMETER= is the length of the outline of a region
        """
        canvas = np.zeros(img.shape, dtype=np.uint8)
        canvas = self.draw_mser_region(canvas, region, "white")
        canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        cnt,_= cv2.findContours(canvas_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        perimeter = cv2.arcLength(cnt[0], True)
        return perimeter

    def ASPECT_RATIO(self, region):
        """
        Calculate aspect ratio of region
        ASPECT_RATIO=width/height
        """
        reshapedRegion = np.reshape(region, (-1, 1, 2))  # reshape for boundingRect method
        x, y, w, h = cv2.boundingRect(reshapedRegion)
        if 0 == h:  # division by zero
            return -1
        aspect_ratio = (1.0 * w) / h
        return aspect_ratio

    def EXTENT(self, region):
        """
        Calculate aspect ratio of region
        EXTENT=pixels of region / rect_area
        """
        reshapedRegion = np.reshape(region, (-1, 1, 2))  # reshape for boundingRect method
        area = len(list(region))  # area= number of pixels in region
        x, y, w, h = cv2.boundingRect(reshapedRegion)
        rect_area = w * h
        if 0 == rect_area:  # division by zero
            return -1
        extent = (1.0 * area) / rect_area
        return extent

    def SOLIDITY(self, region):
        """
        Calculate solidity of region
        SOLIDITY=pixels of region /hull_area
        """
        reshapedRegion = np.reshape(region, (-1, 1, 2))  # reshape for boundingRect method
        area = len(list(region))  # area=Number of pixels in region
        hull = cv2.convexHull(reshapedRegion)
        hull_area = cv2.contourArea(hull)
        if 0 == hull_area:  # division by zero
            return -1
        solidity = (1.0 * area) / hull_area
        return solidity

    def ECCENTRICITY(self, region):
        """
        Calculate eccentricity of region
        The closer to zero, the circle
        The closer to one, the straighter
        ECEENTRICITY=sqrt(1-short axis radius squared/long axis radius squared)
        """
        reshapedRegion = np.reshape(region, (-1, 1, 2))  # reshape for boundingRect method
        x, y, w, h = cv2.boundingRect(reshapedRegion)
        ellipse = cv2.fitEllipse(
            reshapedRegion)  # ((center.x, center.y),( D.b,D.a),angle) where b>a , D.a=short axis diameter of ellipse, D.a=long axis diamerter of ellipse,  dtype=float

        a = round(ellipse[1][1] / 2, 2)  # long axis radius
        b = round(ellipse[1][0] / 2, 2)  # short axis radius

        if 0 == a:  # division by zero
            return -1
        eccentricity = math.sqrt(1 - b ** 2 / a ** 2)
        return eccentricity

    def rectangle_contours(self, img, contours):
        """
        Drawing min area rectangle for contours
        """
        rects = []
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            c = rect[0]
            a = rect[2]
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            rects.append(rect)
        return rects

    def crop_box(self, img, rects):
        """
        if box is skewed, then rotate box straightly and crop
        """
        cropped_box = []
        for rect in rects:
            center = rect[0]
            angle = rect[2]
            # Convert to int
            width = int(rect[1][0])
            height = int(rect[1][1])
            if angle < -45.0:
                angle += 90.0
                width, height = height, width
            # Get rotation matrix for rectangle
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            # Perform rotation on src image
            dst = cv2.warpAffine(img, M, img.shape[:2])
            # Crop box
            sub_img = cv2.getRectSubPix(dst, (width, height), center)
            cropped_box.append(sub_img)
        return cropped_box

    def color_clustering(self, img, k):
        """
        Color clustering for k-means
        """
        img_data = img / 255.0
        img_data = img_data.reshape((-1, 3))

        # K-means clustering
        # Define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        flags = cv2.KMEANS_RANDOM_CENTERS
        img_data = img_data.astype(np.float32)
        compactness, labels, centers = cv2.kmeans(img_data, k, None, criteria, 10, flags)

        new_colors = centers[labels].reshape((-1, 3))
        src_recolored = new_colors.reshape(img.shape)

        # Normalize to show image
        src_recolored = cv2.normalize(src_recolored, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        return src_recolored

    def write_image(self, img, path):
        """
        Write image to directory
        """

    def load_images(self, dirName):
        """
        Load all images from a directory
        """
        # If it is not directory, return None
        images = []
        if False == os.path.isdir(dirName):
            return None
        else:
            absPath = os.path.abspath(dirName)
            for file in os.listdir(dirName):
                _, ext = os.path.splitext(file)
                if '.jpg' == ext or '.png' == ext:
                    images.append(os.path.join(absPath, file))

            return images

    def draw_mser_region(self, canvas, region, color="random"):
        """
            Draw mser(Maximally Stable Extremal Regions) region on black canvas
        """
        np.random.seed()
        # Fill with random colors
        if "random" == color:
            xx = region[:, 0]
            yy = region[:, 1]
            B = np.random.choice((100, 256))
            G = np.random.choice((100, 256))
            R = np.random.choice((100, 256))
            color = [B, G, R]
            canvas[yy, xx] = color
        # Fill with white
        elif "white" == color:
            xx = region[:, 0]
            yy = region[:, 1]
            color = [255, 255, 255]
            canvas[yy, xx] = color

        return canvas

    def image_to_string(self, boxImg, config=('-l kor --oem 3  --psm 7')):
        text = pytesseract.image_to_string(boxImg, config=config)
        return text

    def nms(self, boxes, overlapThresh):
        """
        Remove boxes which are greater than overlapThreshold
        """
        # if it is not ndarray, return None
        if None == isinstance(boxes, np.ndarray):
            return None

        # if there are no boxes, return an empty list
        if 0 == len(boxes):
            return np.empty(0)

        # if the bounding boxes integers, convert them to floats --
        # this is important since we'll be doing a bunch of divisions
        if "i" == boxes.dtype.kind:
            boxes = boxes.astype("float")

        # initialize the list of picked indexes
        pick = []

        # grab the coordinates of the bounding boxes
        x1 = boxes[:, 0]
        y1 = boxes[:, 1]
        x2 = boxes[:, 2]
        y2 = boxes[:, 3]

        # compute the area of the bounding boxes and sort the bounding
        # boxes by the bottom-right y-coordinate of the bounding box
        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        idxs = np.argsort(y2)

        # keep looping while some indexes still remain in the indexes
        # list
        while len(idxs) > 0:
            # grab the last index in the indexes list and add the
            # index value to the list of picked indexes
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)

            # find the largest (x, y) coordinates for the start of
            # the bounding box and the smallest (x, y) coordinates
            # for the end of the bounding box
            xx1 = np.maximum(x1[i], x1[idxs[:last]])
            yy1 = np.maximum(y1[i], y1[idxs[:last]])
            xx2 = np.minimum(x2[i], x2[idxs[:last]])
            yy2 = np.minimum(y2[i], y2[idxs[:last]])

            # compute the width and height of the bounding box
            w = np.maximum(0, xx2 - xx1 + 1)
            h = np.maximum(0, yy2 - yy1 + 1)

            # compute the ratio of overlap
            overlap = (w * h) / area[idxs[:last]]

            # delete all indexes from the index list that have
            idxs = np.delete(idxs, np.concatenate(([last],
                                                   np.where(overlap > overlapThresh)[0])))

        # return only the bounding boxes that were picked using the
        # integer data type
        return boxes[pick].astype("int")


def start(imgPath):
    if os.path.isdir('C:\\Program Files\\Tesseract-OCR'):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    elif os.path.isdir('C:\\Program Files (x86)\\Tesseract-OCR'):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    else:
        print('Cannot find tesseract.exe or set the right path of tesseract.exe')
    assist = Assistant()
    # Generate kernel
    morph_gradient_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 2))

    # Load img
    src = cv2.imread(imgPath)
    origin = src.copy()
    dst = src.copy()

    # K- means color clustering
    src_recolored = assist.color_clustering(src, 3)

    # Convert to gray scale
    gray_src = cv2.cvtColor(src_recolored, cv2.COLOR_BGR2GRAY)

    # MorphGradient operation
    morph_gradient_src = cv2.morphologyEx(gray_src, cv2.MORPH_GRADIENT, morph_gradient_kernel, iterations=1)

    # Calling MSER algorithm
    mser = cv2.MSER_create()
    regions, _ = mser.detectRegions(gray_src)

    # Geometric properties that are used to filter out non-text regions
    candidate_text = []
    for region in regions:
        if assist.ASPECT_RATIO(region) < assist.ASPECT_RATIO_THRESHOLD:
            if assist.EXTENT_MIN_THRESHOLD < assist.EXTENT(region) < assist.EXTENT_MAX_THRESHOLD:
                perimeter = assist.PERIMETER(src_recolored, region)
                if assist.COMPACTNESS_MIN_THRESHOLD < assist.COMPACTNESS(region,
                                                                         perimeter) < assist.COMPACTNESS_MAX_THRESHOLD:
                    candidate_text.append(region)

    # Drawing candidate text regions on canvas
    canvas = np.zeros(src_recolored.shape, dtype=np.uint8)
    for region in candidate_text:
        canvas = assist.draw_mser_region(canvas, region, "white")

    # Dilation
    dilation = cv2.dilate(canvas, dilate_kernel, iterations=3)

    # Drawing rectangle for candiate text
    dilation_gray = cv2.cvtColor(dilation, cv2.COLOR_BGR2GRAY)
    cnt, _ = cv2.findContours(dilation_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rects = assist.rectangle_contours(src, cnt)

    # Crop box
    crop_morph = assist.crop_box(morph_gradient_src, rects)
    crop_src = assist.crop_box(src, rects)

    # Apply inception-v3 inference to candidate text
    # Loads label file, strips off carriage return
    texts = []
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile(assist.LABELS_PATH)]

    # load graph from file
    with tf.gfile.GFile(assist.MODEL_PATH, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        image_data_placeholder = tf.placeholder(tf.uint8)
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        for box in zip(crop_morph, crop_src):
            # Feed the image_data as input to the graph and get first prediction
            predictions = sess.run(softmax_tensor,
                                   {image_data_placeholder: box[0]})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            if "text" == label_lines[top_k[0]]:
                texts.append(box[1])

    # Textbox to string and write
    string = []
    for idx, text in enumerate(texts):
        text = cv2.resize(text, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_LINEAR)
        text_gray = cv2.cvtColor(text, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(text_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blockSize=33,
                                       C=0)

        string.append(assist.image_to_string(thresh))

    return string