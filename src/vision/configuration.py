class Configuration(object):
	config_keys = [
		"name", 
		"cache_root", "video_cache_root", "schedule_cache_root", "queue_root", "jobs_root", "depot_root",
		"render_type", "jukebox", "video_cache_only", "ident_media_root"]
	name = property(lambda self: self.__class__.__name__)
	base_path = "/home/phed/code/mltplayout/mltplayout/"
	cache_root = base_path+"cache/"
	depot_root = base_path+"cache/depot/"
	video_cache_root = base_path+"playout/video/"
	schedule_cache_root = base_path+"cache/dailyplan/"
	queue_root = cache_root+"queue/"
	jobs_root = cache_root+"jobs/"
	ident_media_root = base_path+"video/"

	def config_strings(self):
		l = []
		for key in self.config_keys:
			s = "%s: %s" % (key, getattr(self, key))
			l.append(s)
		return '\n'.join(l)

	def config_tuples(self):
		"For JSON serialization"
		l = []
		for key in self.config_keys:
			l.append((key, getattr(self, key)))
		return l

class FKConfiguration(Configuration):
	media_root = "/mnt/new_media/media/"
	render_type = "broadcast"
	jukebox = True
	video_cache_only = False

class DeveloperConfiguration(Configuration):
	media_root = "./repo/testmedia/media"
	video_cache_root = "./repo/video/"
	ident_media_root = "./repo/ident/"
	render_type = ""
	jukebox = True
	video_cache_only = True
	depot_root = "c:/Depot"

configuration = DeveloperConfiguration()

if __name__=="__main__":
	print "Configuration details:"
	print configuration.config_strings()