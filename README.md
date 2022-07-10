# Minimalist Conditional StyleGAN wrapper

---

### Disclaimer

- The wrapper still requires proper testing, don't use if you have limited computational time.
- This repo allows to call FID pytorch implementation so that you don't have to look for it youself. Majority of scientific papers utilize original tensorflow implementation, you might consider using the original if you plan to work with SOTA

---

### Advantages:
- Fixed annoying deprecation warnings
- Easier configuration for both conditional and non-conditional model with `config.json`
- Full functionality preserved, can be used as usual, without wrapper

---

### Requirements: 
- numpy 1.19.5
- tensorflow 1.x
- pytorch_fid

### How to use:
- Preprocess the images into tfrecords
```console
python wrapper.py create_dataset config.json
```
- Train the model
```console
python wrapper.py train config.json
```
- Calculate FID between two image sets
```console
python wrapper.py fid path/to/imageset1 path/to/imageset2
```

### Configuration: 

- `images_dir` - path to the folder containing dataset images
- `num_labels` - number of classes in conditional model, leave 0 for non-conditional
- `output_resolution` - output resolution of the model
- `dataset_mirror_augment` - specify whether you want StyleGAN dataset tool to mirror-augment the images
- `dataset_dict_path` - path to the dict file<br/>
The dictionary has the following form and lists every image and its class in the dataset. For non-conditional model, 'Labels' key can be omitted but the .pkl file of the dict is still required.
```console
mypickle = {"Filenames": list_of_file_paths, "Labels": class_condition_labels}
```
- `model_name` - name of the model for results saves
- `dataset_name` - name of the preprocessed dataset (tfrecords folder
- `num_gpus` - number of gpus used in training
- `total_kimgs` - total number of kimgs to train for. Similar to epoches, 7500 for plausible results, 3000 to test the model. For transfer learning put total final kimgs (e.g. when training from 7000 to 7500, put 7500)
- `output_model_architecture` - logging flag, leave false if you don't want your console flooded
- `resume_snapshot` - for transfer learning, path to the network .pkl weights snapshot
- `resume_kimg` - for transfer learning, new starting kimg value
- `image_snapshot_ticks` - how often image snapshots are saved
- `network_snapshot_ticks` - how often network .pkl snapshots are saved

```json
{
    "images_dir": "../data/holo/",
    "num_labels": 20,
    "output_resolution": 32,

    "dataset_mirror_augment": true,
    "dataset_dict_path": "../data/holo_label.pkl",

    "model_name": "cgan",
    "dataset_name": "anime",
    "num_gpus": 1,
    "total_kimgs": 140,

    "output_model_architecture": false,

    "resume_snapshot": null,
    "resume_kimg": null,
    "image_snapshot_ticks": null,
    "network_snapshot_ticks": null
}
```
