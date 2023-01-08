import os
import argparse

# python3 run_script_with_hidden_param.py -s create_adjacency_list.py -c twitter_api_param.txt

def main(args):

    def create_command_arg_str(path):
        command_line_args_str = ""
        with open(path, "r") as f:
            line = f.readline().replace("\n", "")
            while line:
                param_name, param_value = line.split(":")
                command_line_args_str += "--{} {} ".format(param_name, param_value)
                line = f.readline().replace("\n", "")
        return command_line_args_str

    
    command_line_args_str = create_command_arg_str(args.hidden_command_line_arg_path)

    if args.public_command_line_arg_path is None:
        pass
    else:
        command_line_args_str += create_command_arg_str(args.public_command_line_arg_path)

    os.system("python3 {} {}".format(args.script, command_line_args_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--script", help="script to run", type=str, default="create_adjacency_list.py")
    parser.add_argument("-c", "--hidden_command_line_arg_path", help="where hidden param are stored", type=str)
    parser.add_argument("-p", "--public_command_line_arg_path", help="where public param for are stored", type=str, default=None)
    
    main(parser.parse_args())


