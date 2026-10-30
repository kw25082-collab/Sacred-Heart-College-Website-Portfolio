from bottle import route, run, template, static_file


@route('/')
def index():
    return template('Profile')

@route('/pillar-one')
def pillar_one():
    return template('Pillar-one')


@route('/pillar-two')
def pillar_two():
    return template('Pillar-Two')


@route('/style.css')
def serve_style():
    return static_file('style.css', root='.')

@route('/images/<filename:path>')
def serve_images(filename):
    return static_file(filename, root='./images')


@route('/me.jpg')
def serve_profile_image():
    return static_file('me.jpg', root='.')


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
