from deepface import DeepFace

# result = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
# print(result)

objs = DeepFace.analyze(img_path = "img4.jpg",actions = ['age', 'gender', 'race', 'emotion'])
print(objs)