# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383351978.841778
_template_filename='/media/Files/workspace/school/cis3210 networking/myapp/myapp/templates/main.mako'
_template_uri='main.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" \n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n    <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>Derek Dekroon 0709999</title>\n\n    <!-- Bootstrap core CSS -->\n    <link href="/css/bootstrap.css" rel="stylesheet">\n    <!-- Bootstrap theme -->\n    <link href="/css/bootstrap-theme.min.css" rel="stylesheet">\n\n    <!-- Custom styles for this template -->\n    <link href="/css/theme.css" rel="stylesheet">\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n      <script src="../../assets/js/html5shiv.js"></script>\n      <script src="../../assets/js/respond.min.js"></script>\n    <![endif]-->\n\n    \n  </head>\n\n  <body>\n\n    <!-- Fixed navbar -->\n    <div class="navbar navbar-inverse navbar-fixed-top">\n      <div class="container">\n        <div class="navbar-header">\n          <a class="navbar-brand" href="#">Log in page</a>\n        </div>\n        <div class="navbar-collapse collapse">\n          <ul class="nav navbar-nav">\n            <li><a id=\'logout\' href="/logout">Log Out</a></li>\n          </ul>\n        </div><!--/.nav-collapse -->\n      </div>\n    </div>\n\n    <div class="container theme-showcase">\n\t<div style=\'height:200px;\' id=\'picContainer\'></div>\n    </div> <!-- /container -->\n\n\n    <!-- Bootstrap core JavaScript\n    ================================================== -->\n    <!-- Placed at the end of the document so the pages load faster -->\n    <script src="/js/jquery.js"></script>\n    <script src="/js/bootstrap.min.js"></script>\n    <script src="/js/holder.js"></script> \n    <script type=\'text/javascript\'>\n    function flickrHandler(rsp) {\n      //window.rsp = rsp;\n      var s = "";\n      // http://farm{id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg\n      // http://www.flickr.com/photos/{user-id}/{photo-id}\n      s = "total number is: " + rsp.photos.photo.length + "<br/>";\n    \n      for (var i=0; i < rsp.photos.photo.length; i++) {\n        photo = rsp.photos.photo[i];\n        t_url = "http://farm" + photo.farm + ".static.flickr.com/" + \n          photo.server + "/" + photo.id + "_" + photo.secret + "_" + "t.jpg";\n        p_url = "http://www.flickr.com/photos/" + photo.owner + "/" + photo.id;\n        s +=  \'<a href="\' + p_url + \'">\' + \'<img style="padding:3px;height:200px;width:200px;" alt="\'+ photo.title + \n          \'"src="\' + t_url + \'"/>\' + \'</a>\';\n      }\n      //alert(s);\n      $(\'#picContainer\').html(s);\n    }\n    </script>\n    <script src="http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=98321bf69d4fa7cce3f182ecf1c29376&tags=construction&per_page=5&format=json&jsoncallback=flickrHandler"></script> \n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


