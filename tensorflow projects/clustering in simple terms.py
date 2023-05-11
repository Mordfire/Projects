# Step 1: Randomly pick K points to place K centroids
# Step 2: Assign all the data points to the centroids by distance. The closest centroid to a point is the one it is assigned to.
# Step 3: Average all the points belonging to each centroid to find the middle of those clusters (center of mass). Place the corresponding centroids into that position.
# Step 4: Reassign every point once again to the closest centroid.
# Step 5: Repeat steps 3-4 until no point changes which centroid it belongs to.

#https://www.google.com/url?sa=i&url=https%3A%2F%2Fdata-flair.training%2Fblogs%2Fclustering-in-machine-learning%2F&psig=AOvVaw0neHvZHpAROaGQKHVV171M&ust=1676913672327000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCJD5prCMov0CFQAAAAAdAAAAABAD