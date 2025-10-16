import os, shutil, random

base_dir = "mydata/cats_and_dogs"
output_dir = "dataset/stage1_cats_vs_dogs"

categories = ["cats", "dogs"]
split_ratio = 0.8  # 80% train, 20% val

for category in categories:
    src = os.path.join(base_dir, category)
    images = [f for f in os.listdir(src) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)

    split_index = int(len(images) * split_ratio)
    train_files = images[:split_index]
    val_files = images[split_index:]

    for split_name, file_list in [("train", train_files), ("val", val_files)]:
        dest_dir = os.path.join(output_dir, split_name, category)
        os.makedirs(dest_dir, exist_ok=True)
        for filename in file_list:
            shutil.copy(os.path.join(src, filename), os.path.join(dest_dir, filename))

print("✅ Dataset reorganized successfully.")
