import os
import exifread

class Orthomosaic:
    """ Orthomosaic - A class to hold information from an orthomosaic (geotiff)"""

    def __init__(self, file_loc):
        self.file_location = file_loc
        self.filename = os.path.basename(file_loc)
        self.exif_tags = None
        self.utm_zone = None
        self.epsg = None
        self.offset_x = None
        self.offset_y = None

    def read_exif_data(self):

        with open(self.file_location, 'rb') as f:
            self.exif_tags = exifread.process_file(f, details=False)
            if 'Image Tag 0x87B1' in self.exif_tags:
                utm_data = self.exif_tags['Image Tag 0x87B1'].values
                if utm_data.startswith('WGS 84'):
                    self.utm_zone = utm_data[utm_data.find('zone') + 5:utm_data.find('|')]
            if 'Image Tag 0x87AF' in self.exif_tags:
                utm_data = self.exif_tags['Image Tag 0x87AF'].values
                self.epsg = utm_data[-5]
            if 'Image Tag 0x87AF' in self.exif_tags:
                utm_data = self.exif_tags['Image Tag 0x87AF'].values
                self.epsg = utm_data[-5]
            if 'Image Tag 0x8482' in self.exif_tags:
                utm_data = self.exif_tags['Image Tag 0x8482'].values
                self.offset_x = utm_data[-3][0]
                self.offset_y = utm_data[-2][0]


