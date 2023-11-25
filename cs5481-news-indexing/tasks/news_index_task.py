from config.config import config
from service.news_index_service import index_news


def news_index():
    # index_news(config.cnn_dir)
    # index_news(config.nbc_dir)
    index_news(config.daily_dir)
    index_news(config.bbc_dir)
