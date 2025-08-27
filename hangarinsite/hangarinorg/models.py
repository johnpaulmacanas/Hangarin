from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        class Priority(BaseModel):
          prio_name = models.CharField(max_length=150)
          status = models.CharField(max_length=150)
          choices=[("Pending", "Pending"), ("In Progress", "In Progress"),("Complete", "Complete"),],
          default = "pending"

            def __str__(self):

                return self.prio_name
            
        class Category(BaseModel):
            cat_name = models.CharField(max_length=150)
            status = models.CharField(max_length=150)
            choices=[("Pending", "Pending"), ("In Progress", "In Progress"),("Complete", "Complete"),],
            default = "pending"


            def __str__(self):

                return self.cat_name

        class Task(BaseModel):
            title = models.CharField(max_length=150)
            description = models.CharField(max_length=150)
            deadline = models.CharField(max_length=150)
            status = models.CharField(max_length=150)
            category = models.ForeignKey(College, null=True, blank=True, on_delete=models.CASCADE)
            priority = models.ForeignKey(College, null=True, blank=True, on_delete=models.CASCADE)

            choices=[("Pending", "Pending"), ("In Progress", "In Progress"),("Complete", "Complete"),],
            default = "pending"


            def __str__(self):

                return self.title

         class Note(BaseModel):
            task = models.CharField(max_length=150)
            consent = models.CharField(max_length=150)
            status = models.CharField(max_length=150)
            choices=[("Pending", "Pending"), ("In Progress", "In Progress"),("Complete", "Complete"),],
            default = "pending"


            def __str__(self):


                return self.name

            class SubTask(BaseModel):
            parent_task = models.CharField(max_length=150)
            title = models.CharField(max_length=150)
            status = models.CharField(max_length=150)
            choices=[("Pending", "Pending"), ("In Progress", "In Progress"),("Complete", "Complete"),],
            default = "pending"


            def __str__(self):


                return self.name



