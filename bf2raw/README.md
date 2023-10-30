# Galaxy wrapper for bioformats2raw

The conversion tool [bioformats2raw](https://github.com/glencoesoftware/bioformats2raw) is wrapped as a Galaxy tool.

The tool receives a single microscopy image file as input and converts it into OME-Zarr format.

The input image must be available in the Galaxy history. 

The tool currently does not accept multiple inputs such as an image series or HCS data. Both the input and output correspond to single images.
