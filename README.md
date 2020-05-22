# get-caged
Randomly inject more Cage action into your intrawebs experience 🧠👾🎬🔥



## Pseudo code plan
Our planned pseudo code for hack implementation.

### Frontend
```
find <img tags
sampled random imgs from img-tags (num tbd)
for each sample as img:
   img.src = `://backend-url/cage?height=${img.height}width=${img.width}`
```

### ETL
Pseudo_code
```python
@contextmanager
def process_file(file):
  try:
    yield file
  finally:
    move_file(processed_dir/file.name, file)

def save_image(width, height, aspect_ratio, blob) -> None:
  "Inserts image into our SQLLite database"
  ...

def load_images(...):
  images = files(unprocessed_dir)
  for img in images:
     with process_file(img) as file:
      width, height, aspect_ratio, blob = get_image_data(file)
      save_image(width, height, aspect_ratio, blob)
  return "Success"
```



### Backend
```python
def get_caged_img(target: TargetImageSpec) -> BinaryImgBlob:
    img = find_image(target)
    img = resize(img, target)
    img = crop(img, target)
    return img

@api.get("cage", query_params=(width: int, height: int))
def get_nick_cage_img(params) -> "Stream img":
    target = TargetImageSpec(...params)
    img = get_caged_img(target)
    return Stream(img, ".../jpg")
```
