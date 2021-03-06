from remotecv.image_processor import ImageProcessor
from remotecv.utils import config, logger


class DetectTask:
    queue = "Detect"
    processor = ImageProcessor()

    @classmethod
    def perform(clz, detection_type, image_path, key):
        logger.info('Detecting %s for %s' % (detection_type, image_path))
        image_data = config.loader.load_sync(image_path)
        points = clz.processor.detect(detection_type, image_data)
        result_store = config.store.ResultStore(config)
        result_store.store(key, points)
