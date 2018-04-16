# t: current time, b: start postion, c: change in value, d: duration
# Current: Quad, Cubic, Quart, Quint, Sine, Expo, Circ, Back
# Missing: Elastic, Bounce


import math

linearTween = lambda t, b, c, d : c*t/d + b

def easeInQuad(t, b, c, d):
	t /= d
	return c*t*t + b


def easeOutQuad(t, b, c, d):
	t /= d
	return -c * t*(t-2) + b

def easeInOutQuad(t, b, c, d):
	t /= d/2
	if t < 1:
		return c/2*t*t + b
	t-=1
	return -c/2 * (t*(t-2) - 1) + b


def easeInOutCubic(t, b, c, d):
	t /= d/2
	if t < 1:
		return c/2*t*t*t + b
	t -= 2
	return c/2*(t*t*t + 2) + b

def easeInQuart(t, b, c, d):
	t /= d
	return c*t*t*t*t + b

def easeOutQuart(t, b, c, d):
	t /= d
	t -= 1
	return -c * (t*t*t*t - 1) + b

def easeInOutQuart(t, b, c, d):
	t /= d/2
	if t < 1:
		return c/2*t*t*t*t + b
	t -= 2
	return -c/2 * (t*t*t*t - 2) + b

def easeInQuint(t, b, c, d):
	t /= d
	return c*t*t*t*t*t + b

def easeOutQuint(t, b, c, d):
	t /= d
	t -= 1
	return c*(t*t*t*t*t + 1) + b

def easeInOutQuint(t, b, c, d):
	t /= d/2
	if t < 1:
		return c/2*t*t*t*t*t + b
	t -= 2
	return c/2*(t*t*t*t*t + 2) + b

def easeInSine(t, b, c, d):
	return -c * math.cos(t/d * (math.pi/2)) + c + b

def easeOutSine(t, b, c, d):
	return c * math.sin(t/d * (math.pi/2)) + b


def easeInOutSine(t, b, c, d):
	return -c/2 * (math.cos(math.pi*t/d) - 1) + b

def easeInExpo(t, b, c, d):
	return c * math.pow( 2, 10 * (t/d - 1) ) + b

def easeOutExpo(t, b, c, d):
	return c * ( -math.pow( 2, -10 * t/d ) + 1 ) + b


def easeInOutExpo(t, b, c, d):
	t /= d/2
	if t < 1:
		return c/2 * math.pow( 2, 10 * (t - 1) ) + b
	t -= 1
	return c/2 * ( -math.pow( 2, -10 * t) + 2 ) + b

def easeInCirc(t, b, c, d):
	t /= d
	return -c * (math.sqrt(1 - t*t) - 1) + b

def easeOutCirc(t, b, c, d):
	t /= d;
	t -= 1
	return c * math.sqrt(1 - t*t) + b

def easeInOutCirc(t, b, c, d):
	t /= d/2
	if t < 1:
		return -c/2 * (math.sqrt(1 - t*t) - 1) + b
	t -= 2
	return c/2 * (math.sqrt(1 - t*t) + 1) + b

### not originaly included, untested

def easeInBack(t, b, c, d):
	s = 1.70158
	t /= (d)+.0001
	return c*t*t*((s+1)*t - s) + b

def easeOutBack(t, b, c, d):
	 t/=d+.0001
	 t-=1
	 s = 3.5
	 return c*(t*t*((s+1)*t + s)+ 1) + b

# def easeInOutBack(t, b, c, d):
# 	s = 1.70158
# 	t /= (d/2)+.0001
# 	if t < 1:
# 		return (c/2)*(t*t*(((s*=(1.525))+1)*t - s)) + b
# 	return (c/2)*((t-=2)*t*(((s*=(1.525))+1)*t + s) + 2) + b

def easeInCubic(t, b, c, d):
	t /= (d)+.0001
	return c*t*t*t + b


def easeOutCubic(t, b, c, d):
	t /= (d)+.0001
	t -=1
	return c*(t*t*t + 1) + b

def linear(t, b, c, d):
	return c*t/(d+.0001) + b
