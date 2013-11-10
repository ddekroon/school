# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1384110185.358175
_enable_loop = True
_template_filename = '/media/derek/Files/workspace/school/cis3210 networking/myapp/myapp/templates/main.mako'
_template_uri = 'main.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        range = context.get('range', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" \n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n    <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>Derek Dekroon 0709999</title>\n\n    <!-- Bootstrap core CSS -->\n    <link href="/css/bootstrap.css" rel="stylesheet">\n    <!-- Bootstrap theme -->\n    <link href="/css/bootstrap-theme.min.css" rel="stylesheet">\n\n    <!-- Custom styles for this template -->\n    <link href="/css/theme.css" rel="stylesheet">\n    <!-- Custom styles for this template -->\n    <link href="/css/style.css" rel="stylesheet">\n    <link href="/css/myStyle.css" rel="stylesheet">\n    <link rel="stylesheet" href="/css/jquery-ui.css" />\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n      <script src="../../assets/js/html5shiv.js"></script>\n      <script src="../../assets/js/respond.min.js"></script>\n    <![endif]-->\n    <script src="/js/jquery.js"></script>\n    <script src="/js/bootstrap.min.js"></script>\n    <script src="/js/holder.js"></script> \n    <script src="js/jquery-ui.js"></script>\n\t<script>\n\t\t$(document).ready(function() {\n\t\t\t$( "#search-menu" ).dialog({\n\t\t\tautoOpen: false,\n\t\t\theight: 300,\n\t\t\twidth: 350,\n\t\t\tmodal: true,\n\t\t\tbuttons: {\n\t\t\t  "Get Pictures": function() {\n\t\t\t\t$("#searchForm").submit();\n\t\t\t  },\n\t\t\t  "Cancel": function() {\n\t\t\t\t$( this ).dialog( "close" );\n\t\t\t  },\n\t\t\t}\n\t\t\t});\n\n\t\t\t$( "#searchMenu" ).button().click(function() {\n\t\t\t  $( "#search-menu" ).dialog( "open" );\n\t\t\t});\n\t\t});\n    </script>\n    \n  </head>\n\n  <body>\n\t  \n\t<div id="search-menu" title="Search Flickr">\n      <p class="validateTips">All form fields are required.</p>\n\t\t<form method="post" action="/main" id="searchForm">\n\t\t\t<table>\n\t\t\t\t<tr>\n\t\t\t\t\t<td>\n\t\t\t\t\t\tSearch String\n\t\t\t\t\t</td><td>\n\t\t\t\t\t\t<input class=\'inputField\'  type=\'text\' name=\'inputText\' class="text ui-widget-content ui-corner-all" />\n\t\t\t\t\t</td>\n\t\t\t\t</tr><tr>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t# of Pictures\n\t\t\t\t\t</td><td>\n\t\t\t\t\t\t<select class=\'inputField\' name="numPictures" class="text ui-widget-content ui-corner-all">\n')
        # SOURCE LINE 75
        for x in range(1, 11):
            # SOURCE LINE 76
            __M_writer(u'\t\t\t\t\t\t\t<option value=')
            __M_writer(escape(x))
            __M_writer(u'>')
            __M_writer(escape(x))
            __M_writer(u'</option>\n')
        # SOURCE LINE 78
        __M_writer(u'\t\t\t\t\t\t</select>\n\t\t\t\t\t</td>\n\t\t\t\t</tr>\n\t\t\t</table>\t\n\t\t</form>\n    </div>\n\n    <!-- Fixed navbar -->\n    <div class="navbar navbar-inverse navbar-fixed-top">\n      <div class="container">\n        <div class="navbar-header">\n          <a class="navbar-brand" href="#">Main page</a>\n        </div>\n        <div class="navbar-collapse collapse">\n          <ul class="nav navbar-nav">\n            <li><a href="/">Menu</a></li>\n            <li><a href="#" id=\'searchMenu\'>Search Flickr</a></li>\n          </ul>\n        </div><!--/.nav-collapse -->\n      </div>\n    </div>\n\n    <div class="container theme-showcase">\n')
        # SOURCE LINE 101
        if c.noImages == 1:
            # SOURCE LINE 102
            __M_writer(u'\t\t\t<h2>')
            __M_writer(escape(c.error))
            __M_writer(u'</h2>\n')
        # SOURCE LINE 104
        __M_writer(u'\t\t<div style=\'height:300px;\' id=\'picContainer\'></div>\n    </div> <!-- /container -->\n\n\n    <!-- Bootstrap core JavaScript\n    ================================================== -->\n    <!-- Placed at the end of the document so the pages load faster -->\n    \n    <script type=\'text/javascript\'>\n    function flickrHandler(rsp) {\n      //window.rsp = rsp;\n      var s = "";\n      // http://farm{id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg\n      // http://www.flickr.com/photos/{user-id}/{photo-id}\n      s = "total number is: " + rsp.photos.photo.length + "<br/>";\n    \n      for (var i=0; i < rsp.photos.photo.length; i++) {\n        photo = rsp.photos.photo[i];\n        t_url = "http://farm" + photo.farm + ".static.flickr.com/" + \n          photo.server + "/" + photo.id + "_" + photo.secret + "_" + "t.jpg";\n        p_url = "http://www.flickr.com/photos/" + photo.owner + "/" + photo.id;\n        s +=  \'<a href="\' + p_url + \'">\' + \'<img style="padding:3px;height:200px;width:200px;" alt="\'+ photo.title + \n          \'"src="\' + t_url + \'"/>\' + \'</a>\';\n      }\n      //alert(s);\n      $(\'#picContainer\').html(s);\n    }\n    </script>\n    <script src="http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=954c721991666c743ffe5d4a1e6544f1&tags=')
        # SOURCE LINE 132
        __M_writer(escape(c.inputText))
        __M_writer(u'&per_page=')
        __M_writer(escape(c.perPage))
        __M_writer(u'&format=json&jsoncallback=flickrHandler"></script> \n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


