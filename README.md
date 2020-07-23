# Aforeserve Client Application

### Clone this repository and configure listed things

### Start with executing following commands

```python
pip3 install -r pack.txt
```

### Detailed structure of gui_flask.py (main file)
```python
line 28-86
if:
    XXXX
else:
    XXXX
```
- If else is checking for unique id for the client who is using application is regeistered or not, if client is registered then flow continues otherwise new client would be created.

```python
line 94-110
variable(s) = data(s)
```
- In these lines code is storing basic details of machine and passing it on to server.

```python
@app.route('/')
```
- In this route chatbot is returned to client with machine's clientname

```python
@app.route('/pr')
```
- In this route printer ticket raising and automation is triggered

```python
@app.route('/emailconfig')
```
- In this route email configuration tikcet raising and automation is triggered

```python
@app.route('/passw')
```
- In this route password change request ticket raise and automation is triggered

```python
@app.route('/diskclean')
```
- In this route diskcleanup ticket and raise and automation is triggered

```python
@app.route('/newrequest')
```
- This route is for returning ui when client clicks on new request

```python
@app.route('/confirmnew')
```
- This route is for returning ui when client clicks on confirm detials

```python
@app.route('/systemrelated')
```
- This route is for returning ui if client clicks on System Realted Issue

```python
@app.route('/apprelated')
```
- This route is for returning ui if client clicks on Application Related Issue

```python
@app.route('/osrelated')
```
- This route is for returning ui if client clicks on OS Related Issue

```python
@app.route('/printerrelated')
```
- This route is for returning ui if client clicks on Printer Related Issue

```python
@app.route('/networkrelated')
```
- This route is for returning ui if client clicks on Network Related Issue

```python
@app.route('/knowticket')
```
- In this route client gets details of tickets previously raised by him/her.

```python
@app.route('/newquery')
```
- In this route client can raise query.

#### In most of the routes new ticket is created in ITSM as well as in DataBase and when automation result comes out, status is updated in ITSM as well as in DataBase. When Ticket is created or resolved client always get a acknowledgement mail.