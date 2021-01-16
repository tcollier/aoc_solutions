require 'ruby_figlet'

require_relative 'lib/box'
require_relative 'lib/screen'

class Application
  def initialize
    @end_at = Time.now + 15
  end

  def running?
    Time.now < @end_at + 10
  end

  def draw(width, height, &block)
    time_diff = [0, @end_at - Time.now].max
    time_str = "%0.2f" % [time_diff]
    settings = BoxSettings.new(
      width: 80,
      border_style: BorderStyles::DOUBLE,
      border_settings: BorderSettings.new(bottom: true),
      align: TextAlign::RIGHT,
      padding: BoxPadding.new(top: 1, bottom: 1),
      margin: BoxMargin.new(left: 5, right: 4, top: 3, bottom: 2)
    )
    Box.new(RubyFiglet::Figlet.new(time_str).to_s, settings).draw(width, height, &block)
  end
end

Screen.run(30, Application.new)
