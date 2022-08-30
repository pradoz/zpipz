# One time setup ( per host / environment)

## PYPI test
- add repository to poetry config poetry config repositories.test-pypi https://test.pypi.org/legacy/
- get token from https://test.pypi.org/manage/account/token/
- store token using poetry config pypi-token.test-pypi  pypi-YYYYYYYY
- Note: 'test-pypi' is the name of the repository

## PYPI Production
- get token from https://pypi.org/manage/account/token/
- store token using poetry config pypi-token.pypi pypi-XXXXXXXX

## Build & check
- `poetry build`
- `poetry check`

## Bump version
- `poetry version prerelease`
- `poetry version patch`

## Poetry Publish

### To test-pypi
- `poetry publish --build --repository test-pypi`
- `poetry publish -r test-pypi`

### To (production) PyPi
- `poetry publish --build`


