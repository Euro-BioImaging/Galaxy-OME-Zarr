from bf2raw import CMD
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('executable', default = 'bioformats2raw/bin/bioformats2raw')
parser.add_argument('input', default = 'datahub/filament.tif')
parser.add_argument('output', default = 'datahub/converted3')
parser.add_argument('--series', default = '')
parser.add_argument('--resolutions', default = '1')
parser.add_argument('--tile_height', default = 10)
parser.add_argument('--tile_width', default = 10)
parser.add_argument('--chunk_depth', default = 3)
parser.add_argument('--downsample_type', default = 'SIMPLE')
parser.add_argument('--compression', default = 'null')
parser.add_argument('--max_workers', default = 4)
parser.add_argument('--nesting', required = False)
parser.add_argument('--omefolder', required = False)
parser.add_argument('--droptop', required = False)
parser.add_argument('--dimension_order', required = False)

args = parser.parse_args()

if __name__ == '__main__':
    cmd = CMD(args.executable)
    cmd.add_param(None, args.input)
    cmd.add_param(None, args.output)
    if args.series != 'all':
        cmd.add_param('--series', args.series)
    cmd.add_param('--resolutions', args.resolutions)
    cmd.add_param('--tile_height', args.tile_height)
    cmd.add_param('--tile_width', args.tile_width)
    cmd.add_param('--chunk_depth', args.chunk_depth)
    cmd.add_param('--downsample-type', args.downsample_type)
    cmd.add_param('--compression', args.compression)
    cmd.add_param('--max_workers', args.max_workers)
    if args.nesting == 'yes':
        pass
    else:
        cmd.add_param(None, args.nesting, is_flag = True)
    if args.omefolder == 'yes':
        pass
    else:
        cmd.add_param(None, args.omefolder, is_flag = True)
    if args.droptop == 'no':
        pass
    else:
        cmd.add_param(None, "scale-format-string '%2$d'", is_flag = True)
    if args.dimension_order == "keep_input_order":
        pass
    else:
        cmd.add_param('--dimension-order', args.dimension_order)
    cmd.add_param(None, 'overwrite', is_flag = True)
    cmd.add_param('--debug', 'off')
    cmd.run()

#
# bioformats2raw
# #if str($io_options.input_location.selection) == 'local':
#     #if str($io_options.input_location.input_type.selection) == 'image':
#         $output.extra_files_path/verified_input/neutral  ## here input dir directly points to image file TIFF
#     #elif str($io_options.input_location.input_type.selection) == 'hcs':
#         '$output.extra_files_path/verified_input/test.companion.ome'
#     #end if
# #elif str($io_options.input_location.selection) == 'remote':
#     #if str($io_options.input_location.input_type.selection) == 'image': ## note that this one is in output html
#         '$output.extra_files_path/verified_input/neutral' ## here input dir directly points to image file
#     #elif str($io_options.input_location.input_type.selection) == 'hcs':
#         '$output.extra_files_path/verified_input/test.companion.ome'
#     #end if
# #end if
# '$output.extra_files_path/conversion'
# #if not str($bf2raw_params.series) == 'none':
#     --series $bf2raw_params.series
# #end if
# --resolutions $bf2raw_params.resolutions
# --tile_height $bf2raw_params.tile_height
# --tile_width $bf2raw_params.tile_width
# --chunk_depth $bf2raw_params.chunk_depth
# --downsample-type $bf2raw_params.downsample_type
# --compression $bf2raw_params.compression
# --max_workers $bf2raw_params.max_workers
# $bf2raw_params.nesting
# $bf2raw_params.omefolder
# $bf2raw_params.droptop
# #if not str($bf2raw_params.dimension_order) == 'keep input order':
#     --dimension-order $bf2raw_params.dimension_order
# #end if
# --overwrite
# --debug off;
