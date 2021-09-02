# Gender-and-Age-Detection   <img alt="GitHub" src="https://img.shields.io/github/license/smahesh29/Gender-and-Age-Detection">

# Objective
This project is a fork of https://github.com/smahesh29/Gender-and-Age-Detection used to guess the gender and age of a person using machine learning.

Main changes done here:
* Dockerized the app
* Modified the code to accept a video instead of an image. This creates and outpus frames (jpg images) of any and all detected faces in a video. It outputs the those frames into the `/frames` directory. From there, they could be combined into a video using ffmpeg (see 'Helpful Commandlines' section below).

# Dependencies (If not using the docker image)
```
	pip install opencv-python argparse
```

# Usage
Docker build
```
docker build -t gad .
docker run --rm -it -v <samples-dir>:/samples -v <frames-dir>:/frames gad bash
```

CLI usage
```
python detect.py --video <absolute-path-to-video>
```

# Helpful Commandlines
Convert series of images to a video
```
ffmpeg -framerate 15 -pattern_type glob -i *.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
```

# About the Project
<p>In this Python Project, I had used Deep Learning to accurately identify the gender and age of a person from a single image of a face. I used the models trained by <a href="https://talhassner.github.io/home/projects/Adience/Adience-data.html">Tal Hassner and Gil Levi</a>. The predicted gender may be one of ‘Male’ and ‘Female’, and the predicted age may be one of the following ranges- (0 – 2), (4 – 6), (8 – 12), (15 – 20), (25 – 32), (38 – 43), (48 – 53), (60 – 100) (8 nodes in the final softmax layer). It is very difficult to accurately guess an exact age from a single image because of factors like makeup, lighting, obstructions, and facial expressions. And so, I made this a classification problem instead of making it one of regression.</p>

<h2>Dataset :</h2>
<p>For this python project, I had used the Adience dataset; the dataset is available in the public domain and you can find it <a href="https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification">here</a>. This dataset serves as a benchmark for face photos and is inclusive of various real-world imaging conditions like noise, lighting, pose, and appearance. The images have been collected from Flickr albums and distributed under the Creative Commons (CC) license. It has a total of 26,580 photos of 2,284 subjects in eight age ranges (as mentioned above) and is about 1GB in size. The models I used had been trained on this dataset.</p>

    
# Credit :
** Forked from https://github.com/smahesh29/Gender-and-Age-Detection **

