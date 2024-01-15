from deepface import DeepFace

result = DeepFace.verify( img1_path = "recognition\\Camera\\man.jpg", img2_path = "recognition\\Camera\\iron.jpg")
print(result)

# objs = DeepFace.analyze(img_path = "recognition\\Camera\\iron.jpg",actions = ['age', 'gender', 'race', 'emotion'])
# print(objs)