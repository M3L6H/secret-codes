def vigenere_cipher(msg, keys)
  msg.each_char.with_index.map do |c, i| 
    if UPPER.include? c 
      UPPER[(UPPER.index(c) + keys[(i - ig) % keys.size]) % 26]
    elsif LOWER.include? c
      LOWER[(LOWER.index(c) + keys[(i - ig) % keys.size]) % 26]
    elsif NUM.include? c
      NUM[(NUM.index(c) + keys[(i - ig) % keys.size]) % 10]
    else
      c
    end
  end.join
end

keys = [4, 5, 6, 7, 5, 4]
UPPER = ("A".."Z").to_a
LOWER = ("a".."z").to_a
NUM = ("0".."9").to_a
exit_commands = ["exit", "quit", "q", "end", "stop"]

cmd = ""

while !exit_commands.include? cmd
  puts "Welcome to the Vigenere Cipher Encoder!"
  puts "The following commands are available:"
  puts "\t(e)ncode\t - Encode a message"
  puts "\t(d)ecode\t - Decode a message"
  puts "\t(q)uit\t\t - Quit this application"
  print "Enter command: "
  cmd = gets.chomp.downcase

  case cmd
  when "e", "encode"
    loop do
      puts "\nCurrently using #{keys}. Would you like to change them? (y/N)"
      print "Enter response: "
      cmd = gets.chomp.downcase
      if cmd == "y"
        puts "Changing keys..."
        puts "Please enter a comma-separated list of numbers"
        print "Enter keys: "
        keys = gets.chomp.split(/, */).map(&:to_i)
      else
        break
      end
    end

    puts "Please enter the message to be encoded."
    print "Enter message: "
    msg = vigenere_cipher(gets.chomp, keys)
    puts "The encoded message is: "
    puts msg
    loop do
      puts "Press enter to confirm."
      break if gets == "\n"
    end
  when "d", "decode"
    loop do
      puts "\nCurrently using #{keys}. Would you like to change them? (y/N)"
      print "Enter response: "
      cmd = gets.chomp.downcase
      if cmd == "y"
        puts "Changing keys..."
        puts "Please enter a comma-separated list of numbers"
        print "Enter keys: "
        keys = gets.chomp.split(/, */).map(&:to_i)
      else
        break
      end
    end

    puts "Please enter the message to be decoded."
    print "Enter message: "
    msg = vigenere_cipher(gets.chomp, keys.map { |k| k * -1 })
    puts "The decoded message is: "
    puts msg
    loop do
      puts "Press enter to confirm."
      break if gets == "\n"
    end
  end
end

puts "Goodbye!"
