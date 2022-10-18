imports.gi.versions.Gtk = "3.0";
const { Gtk } = imports.gi;

Gtk.init(null);

let dialog = Gtk.Dialog.new();
dialog.set_title('https://atareao.es');
dialog.add_button('Si', Gtk.ResponseType.YES);
dialog.add_button('No', Gtk.ResponseType.NO);

let box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 10);
dialog.get_content_area().add(box);
let label = Gtk.Label.new('Dime tu nombre');
box.pack_start(label, true, true, 5);
let entry = Gtk.Entry.new();
box.pack_start(entry, true, true, 5);
dialog.show_all();

if(dialog.run() == Gtk.ResponseType.YES && entry.get_text()){
    print(entry.get_text());
}
