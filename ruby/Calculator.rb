puts "====Simple Calculator===="
puts "First number"
e = gets.to_i
puts "Second number"
k = gets.to_i
puts "1)ADD"
puts "2)DIFF"
puts "3)MUL"
puts "4)DIV"
puts "Enter your Choice:"
v = gets.to_i

case v
when 1
 a = e+k
 puts "Sum = #{a}" 
when 2
 a = e-k
 puts "Difference = #{a}" 
when 3
 a = e*k
 puts "Product = #{a}" 
when 4
 a = e/k
 b = e/k
 puts "Quotient = #{a}" 
 puts "Remainder = #{a}" 
else 
 print "Invalid Choice!"
end


#=======================
#      END
