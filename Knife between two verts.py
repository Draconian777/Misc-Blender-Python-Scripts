import bpy
import bmesh


def knife_between_vertices(obj, vertex_index1, vertex_index2):
    """
    Perform a knife cut between two vertices on a selected face of an object.

    Parameters:
        obj (bpy.types.Object): The object to perform the cut on.
        vertex_index1 (int): Index of the first vertex.
        vertex_index2 (int): Index of the second vertex.
    """
    # Ensure the object is in edit mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    # Get the bmesh of the object
    bm = bmesh.from_edit_mesh(obj.data)

    # Retrieve the two vertices
    v1 = bm.verts[vertex_index1]
    v2 = bm.verts[vertex_index2]

    # Ensure both vertices are valid and linked by an edge
    if not (v1 and v2):
        print("One or both vertices do not exist.")
        return

    # Create a new knife cut operation
    bpy.ops.mesh.select_all(action='DESELECT')
    v1.select = True
    v2.select = True
    bpy.ops.mesh.knife_tool(use_occlude_geometry=False)

    # Update the bmesh and refresh
    bmesh.update_edit_mesh(obj.data)


# Usage example
# Replace "YourObjectName" with the name of your object
# Replace 0 and 1 with the indices of the two vertices
obj = bpy.context.scene.objects['YourObjectName']
knife_between_vertices(obj, 0, 1)



---
import bpy
import bmesh

def knife_between_vertices(obj, vertex_index1, vertex_index2):
    """
    Perform a knife cut between two vertices on a selected face of an object.

    Parameters:
        obj (bpy.types.Object): The object to perform the cut on.
        vertex_index1 (int): Index of the first vertex.
        vertex_index2 (int): Index of the second vertex.
    """
    # Ensure the object is in edit mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    # Get the bmesh of the object
    bm = bmesh.from_edit_mesh(obj.data)

    # Retrieve the two vertices
    try:
        v1 = bm.verts[vertex_index1]
        v2 = bm.verts[vertex_index2]
    except IndexError:
        print(f"One or both vertices do not exist. Ensure indices {vertex_index1} and {vertex_index2} are valid.")
        return

    # Ensure both vertices are linked by an edge (optional validation)
    if not v1 or not v2:
        print("One or both vertices are invalid.")
        return

    # Perform the knife cut
    bpy.ops.mesh.select_all(action='DESELECT')  # Deselect all geometry
    v1.select = True
    v2.select = True
    bm.select_history.clear()
    bm.select_history.add(v1)
    bm.select_history.add(v2)

    # Activate the knife tool
    bpy.ops.mesh.knife_tool(use_occlude_geometry=False)

    # Update the mesh and refresh
    bmesh.update_edit_mesh(obj.data)

# Usage example
# Replace with your object name and vertex indices
obj_name = "mesh[15]_2_2_2_2#-1#4"  # Ensure the name is correct
vertex_1 = 72  # Replace with the index of the first vertex
vertex_2 = 17  # Replace with the index of the second vertex

# Ensure the object exists in the scene
if obj_name in bpy.context.scene.objects:
    obj = bpy.context.scene.objects[obj_name]
    knife_between_vertices(obj, vertex_1, vertex_2)
else:
    print(f"Object '{obj_name}' not found in the scene.")


*************************
knife between Cursor and Vertex

import bpy
import bmesh

def knife_to_cursor(obj, vertex_index):
    """
    Perform a knife cut from a vertex to the 3D cursor location on a selected face of an object.

    Parameters:
        obj (bpy.types.Object): The object to perform the cut on.
        vertex_index (int): Index of the vertex to cut from.
    """
    # Ensure the object is in edit mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    # Get the bmesh of the object
    bm = bmesh.from_edit_mesh(obj.data)

    # Retrieve the vertex
    try:
        v1 = bm.verts[vertex_index]
    except IndexError:
        print(f"Vertex {vertex_index} does not exist.")
        return

    # Ensure the vertex is valid
    if not v1:
        print("Vertex is invalid.")
        return

    # Get the 3D cursor location in the local space of the object
    cursor_location_global = bpy.context.scene.cursor.location
    cursor_location_local = obj.matrix_world.inverted() @ cursor_location_global

    # Create a temporary vertex at the cursor location
    temp_vertex = bm.verts.new(cursor_location_local)
    bm.edges.new([v1, temp_vertex])

    # Update the mesh and refresh
    bmesh.update_edit_mesh(obj.data)
    print(f"Knife cut performed from vertex {vertex_index} to cursor location {cursor_location_local}.")

# Usage example
# Replace with your object name and vertex index
obj_name = "mesh[15]_2_2_2_2#-1#4"  # Ensure the name is correct
vertex_index = 17  # Replace with the index of the vertex to cut from

# Ensure the object exists in the scene
if obj_name in bpy.context.scene.objects:
    obj = bpy.context.scene.objects[obj_name]
    knife_to_cursor(obj, vertex_index)
else:
    print(f"Object '{obj_name}' not found in the scene.")
