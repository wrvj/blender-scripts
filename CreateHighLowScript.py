import bpy

# Get the current selected objects
selected_objects = bpy.context.selected_objects

# Create a new collection named "High"
high_collection = bpy.data.collections.new("High")
bpy.context.scene.collection.children.link(high_collection)

# Unlink the selected objects from their current collections 
for obj in selected_objects:
    for collection in obj.users_collection:
        collection.objects.unlink(obj)
    if not obj.name.endswith("_high"):
        obj.name = obj.name + "_high"
    # Move the selected objects to the "High" collection
    high_collection.objects.link(obj)
    

# Create a new collection named "Low"
low_collection = bpy.data.collections.new("Low")
bpy.context.scene.collection.children.link(low_collection)

for obj in selected_objects:
    duplicated_obj = obj.copy()
    duplicated_obj.data = obj.data.copy()
    
    for collection in duplicated_obj.users_collection:
        collection.objects.unlink(duplicated_obj)
    
    duplicated_obj.name = obj.name.replace("_high", "_low")
    low_collection.objects.link(duplicated_obj)
