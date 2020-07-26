

from pytonik.Flash import Flash

class FlashBootstrap:

    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):
        return None
        
    def __init__(self, *args, **kwargs):
        return None

    def message(self, message, key='flash'):
        return Flash.message(message, key)

    @staticmethod
    def error(title="", description="", dismissible=True, key='flash'):
        title = "<strong>{title}</strong>".format(title=title) if title != "" else ""
        dismissible = """<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
	    """if dismissible == True else "" 
        result = """<div class="alert alert-danger">
        {dismissible}
        {title}{description}
        </div>""".format(title=title, description=description, dismissible=dismissible)
        
        return Flash.message(result, key)

    @staticmethod
    def warning(title="", description="", dismissible=True, key='flash'):
        title = "<strong>{title}</strong>".format(title=title) if title != "" else ""
        dismissible = """<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
	    """if dismissible == True else "" 
        result = """<div class="alert alert-warning">
        {dismissible}
        {title}{description}
        </div>""".format(title=title, description=description, dismissible=dismissible)
        return Flash.message(result, key)
    
    @staticmethod
    def success(title="", description="", dismissible=True, key='flash'):
        title = "<strong>{title}</strong>".format(title=title) if title != "" else ""
        dismissible = """<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
	    """if dismissible == True else "" 
        result = """<div class="alert alert-success">
        {dismissible}
        {title}{description}
        </div>""".format(title=title, description=description, dismissible=dismissible)

        return Flash.message(result, key)

    @staticmethod
    def info(title="", description="", dismissible=True, key='flash'):
        title = "<strong>{title}</strong>".format(title=title) if title != "" else ""
        dismissible = """<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
	    """if dismissible == True else "" 
        result = """<div class="alert alert-info">
        {dismissible}
        {title}{description}
        </div>""".format(title=title, description=description, dismissible=dismissible)
        
        return Flash.message(result, key)

    @staticmethod
    def display(key='flash'):
        return Flash.display(key)