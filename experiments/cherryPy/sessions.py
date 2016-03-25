import cherrypy

sessions = {
    '1': {
        'title': 'Master of Puppets',
        'curator': 'Metallica',
        'genre': 'Metal',
        'key':'C',
        'tempo': '200'
    },

    '2': {
        'title': 'Backseat Freestyle',
        'curator': 'Kendrick Lamar',
        'genre': 'Hip-Hop',
        'key':'D',
        'tempo': '100'
    },

    '3': {
        'title': 'Am I Wrong',
        'curator': 'Anderson Paak',
        'genre': 'Hip-Hop',
        'key':'E',
        'tempo': '125'
    }
}


class Sessions:

    exposed = True

    def GET(self, id=None):

        if id is None:
            return('Here are all the sessions: %s' % sessions)
        elif id in sessions:
            session = sessions[id]

            return(
                'Session with the ID %s is called %s, and the curator is %s' % (
                    id, session['title'], session['curator']))
        else:
            return('No sessions with the ID %s :-(' % id)

    def POST(self, title, curator, genre, key, tempo):

        id = str(max([int(_) for _ in sessions.keys()]) + 1)

        sessions[id] = {
            'title': title,
            'curator': curator,
            'genre': genre,
            'key': key,
            'tempo': tempo
        }

        return ('Create a new session with the ID: %s' % id)

    def PUT(self, id, title=None, curator=None ,genre=None ,key=None ,tempo=None):
        if id in sessions:
            session = sessions[id]

            session['title'] = title or session['title']
            session['curator'] = curator or session['curator']
            session['genre'] = genre or session['genre']
            session['key'] = key or session['key']
            session['tempo'] = tempo or session['tempo']

            return(
                'Session with the ID %s now has the following properties: '
                'title : %s '
                'curator : %s '
                'genre : %s '
                'key : %s '
                'tempo : %s ' % (
                    id, session['title'], session['curator'], session['genre'],
                    session['key'], session['tempo'])
            )
        else:
            return('No session with the ID %s :-(' % id)

    def DELETE(self, id):
        if id in sessions:
            sessions.pop(id)

            return('Session with the ID %s has been deleted.' % id)
        else:
            return('No session with the ID %s :-(' % id)

if __name__ == '__main__':

    cherrypy.tree.mount(
        Sessions(), '/api/sessions',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
         }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
