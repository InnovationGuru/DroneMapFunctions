import utilities as util

def run():
    oms = util.Orthomosaic('NC - Raleigh - Tryon - 20210408 - Ortho.tif')
    oms.read_exif_data()
    print(oms.exif_tags)


run()