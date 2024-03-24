from .common import InfoExtractor


class YourExtractorIE(InfoExtractor):
    _VALID_URL = r"https?://(?:\w+\.)?spwn\.jp/events/(?P<id>[0-9]+-\w+)(?:/streaming)?"
    _TESTS = [
        {
            "url": "https://virtual.spwn.jp/events/24031601-jphololive5thfes",
            "md5": "TODO: md5 sum of the first 10241 bytes of the video file (use --test)",
            "info_dict": {
                # For videos, only the 'id' and 'ext' fields are required to RUN the test:
                "id": "24031601-jphololive5thfes",
                "ext": "mp4",
                # Then if the test run fails, it will output the missing/incorrect fields.
                # Properties can be added as:
                # * A value, e.g.
                #     'title': 'Video title goes here',
                # * MD5 checksum; start the string with 'md5:', e.g.
                #     'description': 'md5:098f6bcd4621d373cade4e832627b4f6',
                # * A regular expression; start the string with 're:', e.g.
                #     'thumbnail': r're:^https?://.*\.jpg$',
                # * A count of elements in a list; start the string with 'count:', e.g.
                #     'tags': 'count:10',
                # * Any Python type, e.g.
                #     'view_count': int,
                "thumbnail": "re:^https?://public-web\.spwn\.jp(?:/[^/]+)+",
            },
        }
    ]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r"<h1>(.+?)</h1>", webpage, "title")

        return {
            "id": video_id,
            "title": title,
            "description": self._og_search_description(webpage),
            "uploader": self._search_regex(
                r'<div[^>]+id="uploader"[^>]*>([^<]+)<',
                webpage,
                "uploader",
                fatal=False,
            ),
            # TODO more properties (see yt_dlp/extractor/common.py)
        }
