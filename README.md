# Object-Detection-in-a-multi-image-scene

“Object detection is the task of jointly localizing and rec- ognizing objects of interest in an image. Specifically, the object detector has to predict a bounding box around each object, and predict the correct object category” (Huang et al., 2021) (p.3).
Our task is to build a deep learning model to perform ob- ject detection using self-supervised or semi-supervised ap- proaches. The dataset provided consists of a mix of labeled and unlabeled data. We’re provided with 30,000 training images, and 20,000 validation images. Both these sets con- sist of 100 classes of common objects such as person, dog, cart, bird, etc. The unlabeled set consists of 512,000 images, which are to be used to learn useful representations that can be subsequently transferred for supervised finetuning on the labeled dataset. The evaluation metric we’re judged on is the Average Precision (AP) computed over a range of Intersection over Union (IoU) values, ranging from 50% to 95% at intervals of 5%.
The best performing model we were able to obtain was a Faster-RCNN model with a MobileNetv3 backbone, achieving an AP[0.50:0.95:0.05] of 25.1% on the hidden test set used to evaluate the performance of each team.
