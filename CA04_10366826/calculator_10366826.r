## Student: 10366826
## Name: Alan Kirwan

## Function 1 - (Addition)

add <- function(x,y){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x+y
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}

## Function 2 - (Subtraction)

subtract <- function(x,y){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x-y
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}
  
## Function 3 - (Multiply)

multiply <- function(x,y){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x*y
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}

## Function 4 - (Divide)

divide <- function(x,y){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    if(y==0){
      stop(NaN)}
    z <- x/y
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}

## Function 5 - (Exponent)

exponent <- function(x,y){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x**y
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}

## Function 6 - (Square)

square <- function(x){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x*x
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}

## Function 7 - (Squareroot)

squareroot <- function(x){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x**0.5
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}

## Function 8 - (Cube)

cube <- function(x){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x**3.0
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}

## Function 9 - (Sine)

sine <- function(x,y){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x/y
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}

## Function 10 - (Cosine)

cosine <- function(x,y){
  number_types <- c('integer', 'numeric', 'complex')
  if(class(x) %in% number_types && class(y) %in% number_types){
    z <- x/y
    z
  } else stop('Either "x" or "y" is not a numeric value.')
}
