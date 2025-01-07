import bpy
import mathutils

# Select your merged object
obj = bpy.context.object
mesh = obj.data

# Collect all vertices in a dictionary with their coordinates
vertex_coords = {}
unique_vertices = []

# Threshold for comparing floating-point positions
threshold = 1e-6

# Find duplicates
for vertex in mesh.vertices:
    rounded_coords = tuple(round(coord, 6) for coord in vertex.co)  # Rounding to avoid precision errors
    if rounded_coords in vertex_coords:
        vertex_coords[rounded_coords].append(vertex.index)
    else:
        vertex_coords[rounded_coords] = [vertex.index]

# Collect unique vertices
for indices in vertex_coords.values():
    if len(indices) == 1:  # Unique vertex
        unique_vertices.extend(indices)

# Delete all vertices except unique ones
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')

# Select non-unique vertices
for vertex in mesh.vertices:
    if vertex.index not in unique_vertices:
        vertex.select = True

# Switch back to edit mode and delete selected vertices
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.delete(type='VERT')
bpy.ops.object.mode_set(mode='OBJECT')

print("Identical vertices removed. Only differences remain.")
