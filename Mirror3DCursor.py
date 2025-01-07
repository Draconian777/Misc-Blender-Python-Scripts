import bpy

# Access the 3D cursor location
cursor_location = bpy.context.scene.cursor.location

# Invert the X-coordinate
cursor_location.x = -cursor_location.x

# Update the 3D cursor location
bpy.context.scene.cursor.location = cursor_location

print(f"3D Cursor X-coordinate inverted. New location: {cursor_location}")


---

#with movement
import bpy
import mathutils

# Mirror the 3D cursor across the X-axis
def mirror_cursor():
    cursor_location = bpy.context.scene.cursor.location

    # Invert the X-coordinate (mirror operation)
    cursor_location.x = -cursor_location.x

    # Update the 3D cursor location
    bpy.context.scene.cursor.location = cursor_location

    print(f"3D Cursor X-coordinate mirrored. New location: {cursor_location}")
    return cursor_location

# Find and move the closest vertex to the cursor
def move_closest_vertex_to_cursor(obj, cursor_location):
    # Ensure the object is in Edit Mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='OBJECT')  # Temporarily switch to Object Mode

    # Get the mesh data
    mesh = obj.data
    closest_vertex = None
    min_distance = float('inf')

    # Find the closest vertex to the cursor location
    for vertex in mesh.vertices:
        distance = (vertex.co - cursor_location).length
        if distance < min_distance:
            min_distance = distance
            closest_vertex = vertex

    # Move the closest vertex to the cursor location
    if closest_vertex:
        print(f"Closest vertex found at {closest_vertex.co}, moving to {cursor_location}")
        closest_vertex.co = cursor_location
    else:
        print("No vertices found in the mesh.")

    # Update the mesh
    bpy.ops.object.mode_set(mode='EDIT')  # Return to Edit Mode

# Main function
def main():
    # Mirror the 3D cursor
    cursor_location = mirror_cursor()

    # Ensure you have an active object and it's a mesh
    obj = bpy.context.object
    if obj and obj.type == 'MESH':
        move_closest_vertex_to_cursor(obj, cursor_location)
    else:
        print("Please select a mesh object.")

# Run the main function
main()
