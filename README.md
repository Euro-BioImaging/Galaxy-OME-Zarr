## Galaxy wrapper for bioformats2raw

The conversion tool [bioformats2raw](https://github.com/glencoesoftware/bioformats2raw) is wrapped as a Galaxy tool.

The tool receives a single microscopy image file as input and converts it into OME-Zarr format.

The input image must be available in the Galaxy history. 

The tool currently does not accept multiple inputs such as an image series or HCS data. Both the input and output correspond to single images.

### Testing and running the tool in a local Galaxy instance with Planemo

First clone this repository to your desired path. Let's say it is `~/planemo_tools`
```bash
cd ~/planemo_tools
git clone https://github.com/Euro-BioImaging/Galaxy-OME-Zarr.git
cd Galaxy-OME-Zarr
```

Let's assume your local Galaxy instance is located at: `</your/galaxy_root>`

To test the tool, make sure you are in the Galaxy-OME-Zarr folder and run the following command:
```bash
planemo test --docker --update_test_data --test_data ./testdata --galaxy_root </your/galaxy_root> ./bf2raw/bf2raw.xml
```

Similarly, to run the tool with Planemo, execute the following command:
```bash
planemo serve --docker --galaxy_root </your/galaxy_root> ./bf2raw/bf2raw.xml
```

### Running the tool in a local Galaxy instance without Planemo
This process consists of two steps: 
1) Install the tool to your Galaxy instance. 
2) Configure your Galaxy so that it can run docker containers.

#### Step 1: Install bf2raw to your Galaxy: 

First clone this repository to the tools directory of your Galaxy
(typically `./tools`).

```bash
cd </your/galaxy_root>/tools
git clone https://github.com/Euro-BioImaging/Galaxy-OME-Zarr.git
```

Then modify your `tool_conf.xml` file. If there is no active `tool_conf.xml`, 
then create one from the sample provided by galaxy as follows:
```bash
cp </your/galaxy_root>/lib/galaxy/config/sample/tool_conf.xml.sample </your/desired/config/dir>
mv </your/desired/config/dir>/tool_conf.xml.sample </your/desired/config/dir>/tool_conf.xml
``` 
Replace `</your/desired/config/dir>` with the directory where you wish to keep your config files.

Then add the following section to the `tool_conf.xml` file:
```xml
<section id="Galaxy-OME-Zarr" name="OMEZarTools">
    <section id="bf2raw" name="bioformats2raw">
        <tool file="Galaxy-OME-Zarr/bf2raw/bf2raw.xml" />	  
    </section> 
</section>  
```

Finally modify your `galaxy.yml` by adding the following line to the "galaxy" section:

```yaml
tool_config_file: </your/desired/config/dir>/tool_conf.xml
```

This will enable galaxy to find the `tool_conf.xml`.

#### Step 2: Configure your Galaxy so that it can run docker containers.

Create a `job_conf.xml` file in your config directory:
```bash
touch </your/desired/config/dir>/job_conf.xml
```
Replace `</your/desired/config/dir>` with the directory where you wish to keep your config files.

Add the following content to the job_conf.xml:

```xml
<?xml version="1.0"?>
<job_conf>
    <plugins>
        <plugin id="local" type="runner" load="galaxy.jobs.runners.local:LocalJobRunner" workers="4"/>
    </plugins>
    <destinations default="local">
        <destination id="local" runner="local"/>
        <destination id="docker_local" runner="local">
	    <param id="docker_enabled">true</param>
        </destination>	
    </destinations>
    <tools>
        <tool id="bf2raw" destination="docker_local"/>
    </tools>
</job_conf>
```

Finally add the following line to the "galaxy" section in your `galaxy.yml`:

```yaml
job_config_file: </your/desired/config/dir>/job_conf.xml
```

This will enable galaxy to find the `job_conf.xml`.
