# Python-for-PHP-Developers

Examples of Python and PHP syntaxes compared.

## Lesson 1: Tools &  First Python Program

### Overview

- Use-cases
- Syntax
- Structure of projects
- etc.


### Lesson 1. Python Installation
To start writing Python programs, we need to install Python binaries first.

But, compared to PHP, you do not need to set up a web server or MySQL database setup to run your Python programs.

##### MacOS
https://www.python.org/downloads/macos/

### Lesson 2. Python vs PHP: Main Syntax Differences

### Python

```php
a=5


if a > 5:
    print('Bigger than 5') #This is inline comment 
elif a>=0:
print('In Between 0 amd  5')
else:
print('Negative')

```````

### PHP

```php

$a=5

if ($a > 5){
echo 'Bigger than 5';  #This is inline comment 
}elseif($a>=0){
echo 'In Between 0 amd  5';
}else
{
    print('Negative');
}

```````

#### 1. End of Statement

Python: The end of the statement is a new line
PHP: Requires a semicolon `;` at the end of each statement.

#### 2. Begin/End of Blocks

* Python: Uses indentation (whitespace) and colons : to indicate the beginning and end of code blocks.
* PHP: Uses curly braces {} to define code blocks.

```php
# Python: ":" instead of curly braces
if a > 5:
    print('Bigger than 5')
    print('No, really bigger')
print('This is outside of IF-statement')
````

````php

// PHP: curly braces
if ($a > 5) {
    echo 'Bigger than 5';
    echo 'No, really bigger';
}
echo 'This is outside of IF-statement';
```````

#### 3. Variable Declaration and Types
Both Python and PHP are dynamically typed languages, so you don't need to specify the data type explicitly
Also, in Python, you don't need a $ sign for variables.

However, the languages have different "level of strictness" about data types.

##### PHP Example (loosely typed):
Conversions between types are often handled automatically.

```php
$num = '10';
$result = $num + 5;
````

PHP automatically converts the $num string to a number for the addition.

#### Python (strongly typed):

Type conversions are more strict. The language enforces type constraints, and you must explicitly convert between different types. This example throws a TypeError Exception:

```php
num = '10'
result = num + 5

TypeError: can only concatenate str (not "int") to str

``````

To avoid this error, the num variable must be converted to an integer before explicitly adding it.

```php
num = '10'
result = int(num) + 5
`````

#### 4. String Concatenation: "+" vs "."

Python: Uses the `+` operator for concatenation.

```php
name = 'Divesh'
message = 'Hello, ' + name
````
PHP: Uses the . operator for concatenation.

```php
$name = 'Divesh';
$message = 'Hello, ' . $name
````

#### 5. Conditional Statements: Parentheses
Python: you don't need parentheses ( and ) for conditions.

```php
if a > 5:
    print('Bigger than 5')
`````

PHP: Parentheses are required.

```php
if ($a > 5) {
    echo 'Bigger than 5';
}
````

#### 6.  Conditional Statements: Elif / Elseif

Python: uses the `elif` to check multiple conditions in sequence:

```php
if a > 5:
    print('Bigger than 5')
elif a >= 0:
    print('In between 0 and 5')
````

PHP: uses the `elseif` instead:

```php
if ($a > 5) {
    echo 'Bigger than 5';
} elseif ($a >= 0) {
    echo 'In between 0 and 5';
}
````

#### 7. Logical Operators

Some operators from PHP are named differently in Python.

Specifically, the logical operators `&&` and `||` are called and and or in Python. Similarly, the logical negation operator `!` is named not in Python.


#### Operator (Python)
`and`
`or`
`not`

#### Operator (PHP)
`&&`
`||`
`!`

```php
if a > 5 and b < 10:
    print('Case 1')
elif  not (a<0 or b<0):
print('Case2)    

```