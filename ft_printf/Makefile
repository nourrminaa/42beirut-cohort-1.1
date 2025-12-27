# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nmina <nmina@student.42beirut.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/27 22:00:00 by nmina             #+#    #+#              #
#    Updated: 2025/12/27 21:55:23 by nmina            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a

CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f

SRC =	ft_printf.c \
		ft_print_char.c \
		ft_print_str.c \
		ft_print_ptr.c \
		ft_print_hex.c \
		ft_print_nbr.c \
		ft_print_unsigned.c

SRC_BONUS =	ft_printf_bonus.c \
			ft_print_char_bonus.c \
			ft_print_str_bonus.c \
			ft_print_ptr_bonus.c \
			ft_print_hex_bonus.c \
			ft_print_nbr_bonus.c \
			ft_print_unsigned_bonus.c \
			ft_parse_flags_bonus.c \
			ft_apply_flags_bonus.c

OBJ = $(SRC:.c=.o)
OBJ_BONUS = $(SRC_BONUS:.c=.o)

LIBFT_DIR = libft
LIBFT = $(LIBFT_DIR)/libft.a

all: $(NAME)

$(LIBFT):
	make -C $(LIBFT_DIR)

$(NAME): $(LIBFT) $(OBJ)
	cp $(LIBFT) $(NAME)
	$(AR) $(NAME) $(OBJ)

bonus: $(LIBFT) $(OBJ_BONUS)
	cp $(LIBFT) $(NAME)
	$(AR) $(NAME) $(OBJ_BONUS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJ) $(OBJ_BONUS)
	make -C $(LIBFT_DIR) clean

fclean: clean
	$(RM) $(NAME)
	make -C $(LIBFT_DIR) fclean

re: fclean all

.PHONY: all clean fclean re bonus