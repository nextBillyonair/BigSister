import pickle

"""
Module File to handle easy loading and saving of objects
via pickle
"""

def save(obj, filename):
	try:
		with open(args.model_file, 'wb') as writer:
			pickle.dump(predictor, writer)
	except IOError:
		raise Exception("Exception while writing to the file %s." % filename)        
	except pickle.PickleError:
		raise Exception("Exception while dumping pickle.")


def load(filename):
	obj = None
	try:
		with open(filename, 'rb') as reader:
			obj = pickle.load(reader)
	except IOError:
		raise Exception("Exception while reading the file %s." % filename)
	except pickle.PickleError:
		raise Exception("Exception while loading pickle.")
	return obj