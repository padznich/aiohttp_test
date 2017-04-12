import datetime

import jinja2
import aiohttp_jinja2


def setup_jinja(app):

    env = aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(app["config"].jinja["templ_path"])
    )

    env.globals.update({
        'str': str,
        'enumerate': enumerate,
        'datetime': datetime,
        'len': len,
    })

    # env.filters['json'] = lambda data: asjson.dumps(data)
    #     <li>
    #       //Example of json template filter:
    #       {{[{'curent': {'utc_time': datetime.datetime.utcnow()}}] | json}}
    #     </li>
    # env.filters['markdown'] = misaka.html
    #     {{readme | markdown}}

    return env
