from poisson_disc import poisson_disc
import random
import xy

# Generate the poisson_disc with paired points, and produce a drawing object from it
random.seed(1337)
r = 0.70
n = 12
points, pairs = poisson_disc(0, 0, 120, 120, r, n)
drawing = xy.Drawing(pairs)
print 'Raw number of paths: %s' % len(drawing.paths)

# Merge the lines and see how much it's reduced
drawing = drawing.linemerge()
print 'Paths after linemerge: %s' % len(drawing.paths)

# Sort the paths and join them, optimized for the xy plotter
paths = drawing.paths
paths = xy.sort_paths_greedy(paths)
paths = xy.join_paths(paths)
print 'Paths after xy optimization: %s' % len(paths)

for tolerance in [0, 1]:
	print ('Simplyfiying based on tolerance %s' % tolerance)
	simplified_paths = paths
	if tolerance:
		simplified_paths = xy.simplify_paths(paths, tolerance=tolerance)
		
	print ('Drawing...')
	drawing = xy.Drawing(simplified_paths)
	im = drawing.render()
	im.write_to_png('test_t%s_n%s_r%s.png' % (tolerance, n, r))

xy.draw(paths, tolerance=1)
