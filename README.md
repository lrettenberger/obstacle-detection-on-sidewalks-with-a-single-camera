# Obstacle Detetion On Sidewalks With A Single Camera

Project repository, which evaluates wheter it is possible to detect obstacles on sidewalks without retraining if the data has been trained on data captured from a camera rig attachted to a car.

* The [StixelNet](http://www.bmva.org/bmvc/2015/papers/paper109/paper109.pdf) is used as the network architecture.
* The Network is trained on the  [KITTI dataset](http://www.cvlibs.net/datasets/kitti/).
* To be applicable to simple mobile-phone cameras only stereo vision is used (i.e. a single camera, not a pair of two cameras).
* The data for transfer learning is a novel dataset created for this project and can be found [here](./sidewalk-dataset).
* Details and Results can be found [here](./report.pdf).
