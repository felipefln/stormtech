class Books(Resource):
    dataset = '''
    [{
        "key": "Book1",
        "author": "Deitel & Deitel",
        "title": "Java How to Program",
        "edition": "2007"   
    },
    {
        "key": "Book2",
        "author": "Martin Fowler",
        "title": "Patterns of Enterprise Application Architecture",
        "edition": "2002"   
    },
    {
        "key": "Book3",
        "author": "Elisabeth Freeman",
        "title": "Head First Design Patterns",
        "edition": "2004"   
    },
    {
        "key": "Book4",  
        "author": "Deitel & Deitel",
        "title": "Internet & World Wide Web: How to Programx",
        "edition": "2007"   
    }]
    '''

    def isDesc(self, param):
        if str(param) == str("asc"):
            return False
        else:
            return True

    def results(self, *args):
        dataset = json.loads(self.dataset)
        items = []
        response = []
        args = args[0]
        if not args:
            return []

        for item in dataset:
            items.append((item['title'], item['author'], item['edition'], item))

        try:
            title_asc = self.isDesc(args["title"])
            items.sort(key=lambda t: t[0], reverse=title_asc)

        except:
            pass

        try:
            author_asc = self.isDesc(args["author"])
            items.sort(key=lambda t: t[1], reverse=author_asc)
        except:
            pass

        try:
            edition_asc = self.isDesc(args["edition"])
            items.sort(key=lambda t: t[2], reverse=edition_asc)
        except:
            pass

        for i in items:
            print(i[3]['key'])
            print(i[3])

        return items

    def post(self):
        content = request.get_json(silent=True)
        response = self.results(content)
        json.dumps(response)


api.add_resource(Books, '/')

if __name__ == '__main__':
    app.run(debug=True)