from student_management_app.models import YourModel

# Retrieve the records that you want to update
your_filtering_criteria={''}
records_to_update = YourModel.objects.filter(your_filtering_criteria)

# Loop through the records and update the date and time fields
for record in records_to_update:
    record.date_field = new_date_value
    record.time_field = new_time_value
    record.save()
