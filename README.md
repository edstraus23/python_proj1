# Flask Content Management System (python_proj1)

This project creates a content management system using Flask as its Python-based web framework. It uses sqlite for the database and Sphinx to produce the output.

## Quick Start Instructions

### Install Application

To install application:

1. Download zip file (Code > Download Zip).

2. Unzip file into a folder.


### Running Application

To run the Flask CMS application:

1. Change directory to the folder where you installed the application.

2. Run the following command in a command window::

```
     python flask_cms.py
```

### Creating New Form

Here are quick instructions for creating a Form in the Flask CMS:

1. Select **Form > Enter New Form**.

2. Fill in form information: Title, Form Name, Categories, etc.

![image](https://github.com/edstraus23/python_proj1/blob/main/images/new_form.png)

   The information that you add will be used a titles for the form input fields.

3. Click **submit**.

   This step will create a directory and the record to the database. It also creates an 'images' directory. 
   
 ```
      result : Created directory: static/italy. Record successfully added. 
      Run 'sphinx-quickstart' on new directory.
 ```

### Running sphinx-quickstart

To run sphinx-quickstart:

1. Change directory to the directory created above.

```
      cd /home/user_name/python_proj1/static/italy
```

2. Run 'sphinx-quickstart'.
   
```
      sphinx-quickstart
```

   Respond to the prompts. You can use default selections. This will create a conf.py, index.rst, and other files and directories.

3. (Optional) Open conf.py in your editor and change the html_theme from 'alabaster' to 'sphinx_rtd_theme'.

```
      html_theme = 'sphinx_rtd_theme'
```

  Note: You may need to install sphinx_rtd_theme (pip install sphinx_rtd_theme).

### Copying Images to images Directory

1. Copy images to images directory (e.g., /home/username/static/italy/images).

### Adding Form to Category List

1. Add the following text to the cat1.csv file:

```
  form,Form
  topicmap,Topicmap
  bookmap,Bookmap
  images,Images
  althete,Favorite Athletes
  movies,Favorite Movies
  recent_movies,Recently Viewed Movies
  baseball,Favorite Baseball Players
  tv_shows,TV Shows
  quickstart,Quick Start
  italy, Italy
```

### Creating Topics

To create a topic for your form:

1. Select **Forms > Display Forms**.

![image](https://github.com/edstraus23/python_proj1/blob/main/images/display_stories.png)
 
2. Click on [add_entry].

3. Fill in the form. For this example, we will use 'Colosseum' as the file 

4. For the Contents field, enter restructured text. For example:

``` rst

     *************
     Colosseum 
     *************

     The following is a photo of the Colosseum in Rome:

     .. image:: images/italy1.jpg
      :width: 400px
      :align: center
      :alt: Colosseum in Rome

      We visited Rome in late March of 2018.
```
   
   This will create a Colosseum.rst file in the 'static/italy' folder.

5. Follow steps 1 - 3. Use index as the file name when creating topic.

6. Edit index.rst file to include the Colosseum file:

``` rst

      .. Italy documentation master file, created by
         sphinx-quickstart on Thu Apr  9 14:59:34 2020.
         You can adapt this file completely to your liking, but it should at least
         contain the root `toctree` directive.

     Welcome to Italy's documentation!
     =================================

     .. toctree::
        :maxdepth: 2
        :caption: Contents:
     
        Colosseum


     Indices and tables
     ==================

     * :ref:`genindex`
     * :ref:`modindex`
     * :ref:`search`
 ```

### Build Html Files

1. Run the following command to build the html files:

 ```
      make build
 ```

2. This creates the html files in the /home/eric/newproj/static/italy/_build/html directory.

3. Open Colosseum.html. You should see something like the following:

![image](https://github.com/edstraus23/python_proj1/blob/main/images/italy_output.png)
