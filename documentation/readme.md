on click tab
call function to get url page
on page get bind form submit
on submit, submit via ajax
???


on delete, remove images of user
@receiver(post_delete, sender=Photo)
def delete_photo_from_dir(sender, instance, args, kwargs):
if os.path.exists(instance.dir):
	os.remove(instance.dir)



list dir
os.scandir(path='.')
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)


os.DirEntry
