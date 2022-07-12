# LAP 4 Debugging Assignment

## Installation & usage
To quickly run the developement version of this site:
- Clone or download the repo.
- Open terminal and navigate to `auguste-lap4-debug-millman97` folder.
- Run `bash _scripts/startDev.sh`.
- Enter the pipenv shell with `pipenv shell` and install any dependencies with `pipenv install`.
- Finally, run the server with `pipenv run dev`

You will be able to access the server from `http://localhost:5000/`.

To stop running the app, enter `CTRL+C` in the terminal to exit the server and run `docker compose down`.

## Changelog
1. Add if name = main guard to wsgi.py
2. Add CORS to app
3. Import pytest and app to tests
4. Add Home title param to its route
5. Add Thank You title param to its route
6. Add text to navbar buttons
7. Add content block to layout
8. Import mail_config correctly (had previously imported an incorrect version to get a base version of the site working)
9. Add custom error pages for error codes 404, 405 and 500
10. Add titles to error pages according to spec
11. Fix test file fixtures
12. Add eventlisteners to enable buttons on input change
13. Add mailtrap.io details to test the site works
14. Change title on prediction submit to results
15. Change eventlistener to input to better reflect spec
16. Add test for 404 error
17. Update readme.md
18. Remove console logs

## Bugs
Currently no known bugs

## Wins and Challenges
The biggest challenge was understanding how the predictor and mailing functions work.

The biggest win was getting the functionality working and seeing an email in my mailtrap.io inbox.
