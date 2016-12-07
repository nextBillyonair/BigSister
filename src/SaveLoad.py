import pickle

"""
Module File to handle easy loading and saving of objects
via pickle
"""

def save(obj, filename):
	"""
	Saves an object (obj) to filename via pickle.dump
	Throws IOError if cannot write to filename.
	Throws PickleError is pickle cannot dump obj.
	"""
	try:
		with open(filename, 'wb') as writer:
			pickle.dump(obj, writer)
	except IOError:
		raise Exception("Exception while writing to the file %s." % filename)        
	except pickle.PickleError:
		raise Exception("Exception while dumping pickle.")


def load(filename):
	"""
	Loads an item from filename.
	Returns the object that was saved in filename.
	Throws IOError if File DNE.
	Throws PickleError is file cannot be opened via pickle.
	"""
	obj = None
	try:
		with open(filename, 'rb') as reader:
			obj = pickle.load(reader)
	except IOError:
		raise Exception("Exception while reading the file %s." % filename)
	except pickle.PickleError:
		raise Exception("Exception while loading pickle.")
	return obj