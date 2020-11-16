class Cipher
  ALPHABET_UPPER = ("A".."Z").to_a
  ALPHABET_LOWER = ("a".."z").to_a
  NUMBERS = ("0".."9").to_a
  
  def initialize
    @message = ""
    @mode = :decode
    @negate = false
    @offset = 2

    self.parse_args(ARGV)
    self.encode
  end

private
  attr_accessor :message, :mode, :negate, :offset

  # Functionally only the encode method is needed, since decoding is just
  # encoding in reverse
  def encode
    self.offset *= -1 if self.negate
    offset = self.offset

    # We invert the offset used if we are trying to decode the message
    offset *= -1 if self.mode == :decode

    msg = self.message.chars.map do |ch|
      case ch
      when "A".."Z"
        idx = ALPHABET_UPPER.index(ch)
        ALPHABET_UPPER[(idx + offset) % 26]
      when "a".."z"
        idx = ALPHABET_LOWER.index(ch)
        ALPHABET_LOWER[(idx + offset) % 26]
      when "0".."9"
        idx = NUMBERS.index(ch)
        NUMBERS[(idx + offset) % 10]
      else
        ch
      end
    end.join

    self.print <<~HEREDOC
    Message #{ self.mode == :decode ? "decoded" : "encoded" } with offset #{ self.offset }:

    #{ msg }
    HEREDOC
  end

  # Command line interpretation
  def parse_args(args)
    self.print_help if args.empty?

    parsing_file = false
    parsed_file = false
    parsing_message = false
    parsing_offset = false

    for arg in args
      if parsing_offset
        self.offset = arg.to_i

        if self.offset == 0
          raise ArgumentError.new("Expected a valid integer offset not equal to 0")
        end
        
        parsing_offset = false
        next
      elsif parsing_file
        f = File.open(arg)
        self.message = f.read
        f.close
        parsing_file = false
        parsed_file = true
        next
      elsif parsing_message
        self.message += " #{ arg }"
        next
      end

      case arg
      when /^[^-].*$/
        return if parsed_file
        self.message = arg
        parsing_message = true
      when "--decode", "-d"
        self.mode = :decode
      when "--encode", "-e"
        self.mode = :encode
      when "--help", "-h"
        self.print_help
      when "--negative", "-n"
        self.negate = true
      when "--offset", "-o"
        parsing_offset = true
      when "--path", "-p", "--file", "-f"
        parsing_file = true
      else
        self.print_help
      end
    end
  end

  # Print the help message
  def print_help
    print <<~HEREDOC
      Usage: ruby caesar_cipher.rb [options] [message string]
      \t-d, --decode
      \t\tset the program to decode (default is decode)
      \t-e, --encode
      \t\tset the program to encode (default is decode)
      \t-f=FILEPATH, --file=FILEPATH
      \t\tset a file to read from
      \t-h, --help
      \t\tprint this message
      \t-n, --negative
      \t\tnegate the offset. Can also pass a negative offset
      \t-o=NUMBER, --offset=NUMBER
      \t\tset the offset used by the cipher. Default is 2
      \t-p=FILEPATH, --path=FILEPATH
      \t\tsee -f
    HEREDOC
  end

  # Prints the passed message and exits the program
  def print(msg)
    puts msg
    exit(0)
  end
end

Cipher.new