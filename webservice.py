import json

from klein import Klein
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound


class RestAPI:
    app = Klein()
    students = {}
    fields = ("name", "courses")
    
    def response(self, request, status=200, **kwargs):
        """
        Build the response body as JSON and set the proper content-type
        header.
        """
        request.setResponseCode(status)
        if kwargs:
            request.setHeader("Content-Type", "application/json")
            return json.dumps(kwargs)
    
    def getStudentOr404(self, studentID):
        try:
            return self.students[studentID]
        except KeyError:
            raise NotFound
    
    def getStudentFromRequest(self, request, complete=True):
        """
        Read a student from the request body in JSON format and retrieve
        a dictionary. If `complete` is `False`, a 400 Bad Request error
        will be raised if the read student is missing some of the
        `self.fields` elements.
        """
        try:
            student = json.loads(request.content.read())
        except json.decoder.JSONDecodeError:
            raise BadRequest("Could not decode body as JSON")
        # Every key must be a valid field name.
        for key in student:
            if key not in self.fields:
                raise BadRequest(f"Unknown field: {key}")
        if complete:
            for field in self.fields:
                if field not in student:
                    raise BadRequest(f"Missing field: {field}")
        return student
    
    @app.handle_errors(NotFound)
    def notFoundHandler(self, request, failure):
        """
        Called when a 404 not found is raised.
        """
        return self.response(request, status=404)
    
    @app.handle_errors(MethodNotAllowed)
    def methodNotAllowedHandler(self, request, failure):
        """
        Called when a 405 is raised.
        """
        return self.response(request, status=405)
    
    @app.handle_errors(BadRequest)
    def badRequestHAndler(self, request, failure):
        """
        Called when a 400 is raised. Get the exception description and
        move it to the response's `reason` key in JSON format.
        """
        return self.response(
            request, status=400, reason=failure.value.description)
    
    @app.route(
        "/student",
        methods=["GET", "POST"],
        defaults={"studentID": None}
    )
    @app.route(
        "/student/<int:studentID>",
        methods=["GET", "PUT", "DELETE"]
    )
    def student(self, request, studentID):
        if request.method == b"POST":
            student = self.getStudentFromRequest(request)
            try:
                newID = max(self.students.keys()) + 1
            except ValueError:
                newID = 1
            self.students[newID] = student
            return self.response(request, status=201, id=newID)
        
        elif request.method == b"GET":
            if studentID is None:
                return self.response(
                    request,
                    students=[{"id": k, **v} for k, v in self.students.items()]
                )
            return self.response(
                request,
                student=self.getStudentOr404(studentID)
            )
        
        elif request.method == b"PUT":
            student = self.getStudentOr404(studentID)
            newData = self.getStudentFromRequest(request, complete=False)
            student.update(newData)
            return self.response(request, status=204)
        
        elif request.method == b"DELETE":
            try:
                del self.students[studentID]
            except KeyError:
                raise NotFound
            return self.response(request, status=204)


if __name__ == "__main__":
    api = RestAPI()
    api.app.run("localhost", 7001)
