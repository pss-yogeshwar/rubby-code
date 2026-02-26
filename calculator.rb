puts "=== Simple Ruby Calculator ==="

print "Enter first number: "
a = gets.to_f

print "Enter operator (+, -, *, /): "
op = gets.chomp

print "Enter second number: "
b = gets.to_f

result = 0

case op
when "+"
  result = a + b
when "-"
  result = a - b
when "*"
  result = a * b
when "/"
  if b != 0
    result = a / b
  else
    puts "Cannot divide by zero"
    exit
  end
else
  puts "Invalid operator"
  exit
end

puts "Result = #{result}"
