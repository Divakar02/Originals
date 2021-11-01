dict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}
subject=input("Enter the subject: ")
x=dict["class"]["student"]["marks"][subject]
print(x)